# the_hidden_one

usage: hideme [-h] [-i] [-c] [-p PASSWORD] [-s SALT] [-im IMAGE] [-te TEXTENCRYPT] [-fe FILEENCRYPT] [-td TEXTDECRYPT] [-fd FILEDECRYPT] [-th TEXTHIDE] [-fh FILEHIDE] [-tr TEXTREVEAL] [-fr FILEREVEAL]
              [-ae AESENCRYPT] [-ad AESDECRYPT]

Cryptography And Steganography Script.

options:
  -h, --help            show this help message and exit
  -i, --interactive     hideme -i (Starts Script In Interactive Mode.)
  -c, --clean           hideme --clean (Delete Unnecessary Files.)
  -p PASSWORD, --password PASSWORD
                        hideme -p password (Pass Password For Encryption And Decryption.)
  -s SALT, --salt SALT  hideme -s salt (Pass salt For Decryption.)
  -im IMAGE, --image IMAGE
                        hideme -im image location (Image To Hide Text/File.)
  -te TEXTENCRYPT, --textencrypt TEXTENCRYPT
                        hideme -te 'some text' -p password (Encrypt The Text. Dont Forget To Pass The Text Inside Quotation)
  -fe FILEENCRYPT, --fileencrypt FILEENCRYPT
                        hideme -fe File Location -p password (Encrypt File.)
  -td TEXTDECRYPT, --textdecrypt TEXTDECRYPT
                        hideme -td Hash -p password -s Salt (Decrypt Hash To Text.)
  -fd FILEDECRYPT, --filedecrypt FILEDECRYPT
                        hideme -fd File Location -p password -s Salt (Decrypt File.)
  -th TEXTHIDE, --texthide TEXTHIDE
                        hideme -th 'some text' -im Image Location (Hide Text in Image.Dont Forget To Pass The Text Inside Quotation)
  -fh FILEHIDE, --filehide FILEHIDE
                        hideme -fh File Location -im Image Location (Hide File in Image.)
  -tr TEXTREVEAL, --textreveal TEXTREVEAL
                        hideme -tr File Location(Reveal Text From Image.)
  -fr FILEREVEAL, --filereveal FILEREVEAL
                        hideme -fr File Location(Reveal File From Image.)
  -ae AESENCRYPT, --aesencrypt AESENCRYPT
                        hideme -ae File Location -p password (Encrypt File AES Mode.)
  -ad AESDECRYPT, --aesdecrypt AESDECRYPT
                        hideme -ad File Location -p password (Decrypt File AES Mode.)
