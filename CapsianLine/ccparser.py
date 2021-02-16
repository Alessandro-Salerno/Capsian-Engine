# ----------------------------------------------------------------------------
# CapsianLine
# Copyright 2021 Carpal
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------


from CapsianLine.cclexer import *
from CapsianLine.ccerror import *


class Parser:
   # the lexer
   lexer = None

   def __init__(self, command) -> None:
      self.lexer = Lexer(command)
   
   # expects a token kind
   def expect(self, kind):
      # take the next token from the lexer
      token = self.lexer.next_token()
      #  token_kind != kind
      if token[0] != kind:
         error(f"expected {Token.pretty_kind(kind)}, found {Token.pretty_idsym(token[0], token[1])}")
      
      return token

   # expects an identifier (VALUE) with a specific value
   def expect_keyword(self, value):
      token = self.lexer.next_token()
      #  token_kind != VALUE         token_value != value
      if token[0] != Token.VALUE and token[1] != value:
         error(f"expected {Token.pretty_idsym(Token.VALUE, value)}, found {Token.pretty_idsym(token[0], token[1])}")
      
      return token

   # expects a symbol with a specific value
   def expect_symbol(self, value):
      # take a token from the lexer
      token = self.lexer.next_token()
      #  token_kind != SYMBOL         token_value != value
      if token[0] != Token.SYMBOL and token[1] != value:
         error(f"expected {Token.pretty_idsym(Token.SYMBOL, value)}, found {Token.pretty_idsym(token[0], token[1])}")
      
      return token

   # expects an arg, if there is other raise an error
   def expect_arg(self):
      # when pass an arg there must be the -arg flag
      # expect -
      self.expect_symbol("-")
      # expect the flag, maybe other flags in the future
      self.expect_keyword("arg")
      
      # returns the value of the next token
      return self.expect(Token.VALUE)[1] # 1 of a tuple with two elements, the first is the token kind, the second the token value

   # collects all the arguments passed until the file ends
   def expect_args(self):
      args = []
      
      # in this way you can also pass no args and it will work because this cycle will never be ran
      # the file is not finished yet ?
      while not self.lexer.reachedEOF():
         # then collect the next arg and append it to the others
         args.append(self.expect_arg())
         
      return args
   
   # organizes the parsing process
   def expect_command(self):
      command = self.expect(Token.VALUE)[1] # 1 = second term of the tuple = the value
      sub_command = self.expect(Token.VALUE)[1]
      args = self.expect_args()
      
      return (command, sub_command, args)

   # returns a tuple containing (class, method, args)
   def parse(self):
      return self.expect_command()