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


from CapsianLine.ccerror import error
from unicodedata         import category


# is a control or a white space (chars to skip) ? like \n \t etc..
def is_control(char):
   return category(char) == "Cc" or str(char).isspace()


# is a symbol ? like +-@/()[]{} etc..
def is_symbol(char):
   return category(char) == "Po" or category(char) == "Pd"


# token kind
class Token:
   # token kinds
   VALUE  = "<ID>"
   SYMBOL = "<SYM>"
   EOF    = "<EOF>"
   BAD    = "<BAD>"


   # short ways
   def value(value):
      return (Token.VALUE, value)


   def eof():
      return (Token.EOF, None)


   def bad():
      return (Token.BAD, None)


   # for errors
   # returns a pretty version of the passed token
   def pretty_idsym(kind, value):
      if kind == Token.VALUE or kind == Token.SYMBOL:
         return value.replace('\n', '\\n').replace('\t', '\\t')

      if kind == Token.EOF:
         return "end of file"

      if kind == Token.BAD:
         return "bad token"
      
      return kind
   

   # returns a pretty version of the passed token kind
   def pretty_kind(kind):
      if kind == Token.EOF:
         return "end of file"

      if kind == Token.BAD:
         return "bad token"

      if kind == Token.VALUE:
         return "value"

      if kind == Token.SYMBOL:
         return "symbol"
      
      return kind


# lexer
class Lexer:
   # the command to lex
   command = None

   # the current index
   index = 0

   # set up
   def __init__(self, command) -> None:
      self.command = command
   

   # checks if there is a next char
   def next_exists(self):
      return self.index + 1 < len(self.command)


   # checks if the command text if finished
   def reachedEOF(self):
      return self.index >= len(self.command)


   # if the eof has not been exceeded returns the current character otherwise an EOF token
   def current(self) -> str:
      # not over the eof ?
      if not self.reachedEOF():
         # then return the current char
         return str(self.command[self.index])

      # else return a eof token
      return str(Token.EOF)
   

   # the same of current(), but with the next character instead of the current
   def next(self) -> str:
      # the current is not the last char in the command text ?
      if self.next_exists():
         # then return the next, but remain at the current position
         return str(self.command[self.index + 1])

      return str(Token.EOF)


   # moves the current position of one
   def advance(self):
      self.index += 1
   
   # skips all the escaped characters in the text
   def eat_controls(self):
      # the current is a valid char and this char is a control ?
      while (not self.reachedEOF()) and is_control(self.current()):
         # then advice while it is that
         self.advance()


   # called if found an identifier char or a number. collects the entire value and returns it
   def collect_value(self):
      ident = ""
      
      while True:
         # add the current char to the string
         ident += self.current()

         # this is the last char or the next char is not a valid char value ?
         if self.reachedEOF() or not self.next().isalnum():
            # then break the collecting
            break
         
         # this char has been collected, let's go to the next
         self.advance()
         
      # return the collected value
      return Token.value(ident)


   # converts a char into its escaped version
   def next_escaped(self):
      # get the char to convert
      char = self.current()
      
      if char == "'": return "'"
      if char == "n": return '\n'
      if char == "t": return '\t'
      if char == "\\": return '\\'

      # this is not a valid escaped char, I don't know what to return, so I raise an error
      error(f"invalid escaped char \\{char}")


   # called after found a quote '. collects the string until it finds another quote or the end of the file
   def collect_string(self):
      string = ""
      
      # skip first quote '
      self.advance()

      while True: # do while missing in python, shit!
         # match escaped chars
         if self.current() == "\\":
            # skip the \ espace char
            self.advance()
            # add to the string the next character converted to a real escaped char
            string += self.next_escaped()
         else:
            # not an escaped char ? add it to the string as a normal char
            string += self.current()

         # the user opened the string quote, but he never closed it, this is wrong
         if self.reachedEOF():
            error("string opened and never closed")

         # after collected the previously char, move to the next
         self.advance()

         # the next was a string quote ?
         if self.current() == "'":
            # break the string collecting
            break
      
      # return the string as a value
      return Token.value(string)


   # returns eof if the index is at the end of the file, so there is no char to process
   def next_token(self) -> Token:
      # skip all controls
      self.eat_controls()

      token = None
      
      # there is not char to process ?
      if self.reachedEOF():
         return Token.eof()
      
      # this char is a num or a letter ?
      if self.current().isalnum():
         # then collect it
         token = self.collect_value()

      elif self.current() == "'":
         # collect the string
         token = self.collect_string()
      
      # a symbol ?
      elif is_symbol(self.current()):
         token = (Token.SYMBOL, self.current())
      
      # none of the priors?
      else:
         token = Token.bad()
      
      # next char
      self.advance()
      return token
