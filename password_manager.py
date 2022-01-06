import csv, os, sys, json, random, string
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

password_file_name = "passwords" ### Defining database name
salt_value = 7 ### Defining salt value for key generation

### This function encodes password json object into 'utf-8' byte
def dictToBytes(password_object):
	return json.dumps(password_object).encode('utf-8')
	
### This function decodes 'utf-8' byte into password json object
def bytesToDict(password_object_byte):
	return json.loads(password_object_byte.decode('utf-8'))

### This function encrypts every entry and stores them in the database file
def encrypt(password_object_byte, key):
	encryption_key = key[:32] ###Defining key for encryption
	iv = key[-16:] ### Defining initialization vector for AES encryption
	
	counter = Counter.new(128, initial_value = bytes_to_long(iv)) ### Defining counter for AES encryption based on initialization vector
	cipher = AES.new(encryption_key, AES.MODE_CTR, counter = counter) ### Defining AES encryption object
	
	ciphertext = cipher.encrypt(password_object_byte) ### Encrypting the entries using AES encryption object
	
	with open(password_file_name, 'wb') as outfile: ### Writing the encrypted entries to the database
		[outfile.write(ciphertext) ]
		
def decrypt(key):
		decryption_key = key[:32] ###Defining key for decryption
		iv = key[-16:] ### Defining initialization vector for AES decryption
		
		counter = Counter.new(128, initial_value = bytes_to_long(iv)) ### Defining counter for AES decryption based on initialization vector
		cipher = AES.new(decryption_key, AES.MODE_CTR, counter = counter) ### Defining AES decryption object
	
		with open(password_file_name, 'rb') as infile: ### Reading all entries from database file
			ciphertext = [ infile.read() ]
		
		for x in ciphertext: ### Decrypting the entries one by one
			decrypted_data = cipher.decrypt(x)
	
		return decrypted_data

def Main():
	
	### Check for incorrect input
	if len(sys.argv)  != 2:
		print("Missing argument...")
		print("Program running command should look like following...\n")
		print("python pwMan.py <website>")
		return
	
	master_password = input("Enter Master Password: ")
	key = PBKDF2(master_password, salt_value, dkLen=48) ### Generating key from master password
	
	if not os.path.isfile(password_file_name): ### Checking if the database is created or not
		print("No password database found, creating a database....\n")
		password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)]); ### Generating random password for individual entry
		password_object = {}; ### Declaring password json object
		password_object[sys.argv[1]] = password ### Storing randomly generated password into password object for particular entry
		password_object_byte = dictToBytes(password_object) ### Encoding password object to 'utf-8' format
		encrypt(password_object_byte, key) ### Encrypting 'utf-8' formated password object and storing the object to database file
		print("Database created and first entry added.")
	else:
		try: ### Checking for incorrect master password
			print("Loading database...\n")
			password_object_byte = decrypt(key) ### Decrypting the database file and retrieving all the 'utf-8' formatted entries
			password_object = bytesToDict(password_object_byte) ### Converting 'utf-8' formatted entries to password json object

		except Exception as e: ### Displaying error message for incorrect password
			print("Wrong password")
			return
			
		entry = sys.argv[1] ### Defining variable to store the entry for which the used asked for
		if entry in password_object: ### Checking if the user entry exists in the database or not
			print("Entry   : " + str(entry))
			print("Password: " + str(password_object[entry]))
		else: ### If the user entry does not exist in the database then new entry in the database will be created
			print("No entry for " + str(entry) + " found, creating new entry...\n")
			password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)]); ### Generating random password for new entry
			password_object[entry] = password ### Storing newly generated password to existing password object
			encrypt(dictToBytes(password_object), key) ### Encoding password object to 'utf-8' format, then encrypting the password object and finally storing updated encrypted password object to existing database file
			print("New entry stored.")


if __name__ == '__main__':
	print("\n\nWelcome to Password Manager program.\n\n")
	Main()

