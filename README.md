# Encrypted Password Manager
The project generates password for given websites and stores them in a file encrypted with AES 256 key in counter mode. It uses a master password and a salt value to generate the key and initialization vector. To generate the key and initialization vector the project uses PBKDF2 (Password-Based Key Derivation Function 2). A 256-bit key and 128-bit initialization vector are created through PBKDF2. The website and it’s password are stored as a json object in the memory encode in utf-8 format. Then, the json object is encrypted by AES and stored in the password file. When a password for given website is already stored in the password file then upon receiving a website name the project retrieves the password from the password file. Then the password is decoded to json object by decoding utf-8 format. After that, AES decryption is being done and the password is shown in plain text along with the website name. The project uses python 3 and needs pycryptodome library to run. The project execution flow is given below.

When running the project, it requires a website. It will ask repeatedly until a website name is given like below.

![fig1](https://user-images.githubusercontent.com/3108754/148324089-3b8c3349-0cc3-459a-8a63-5008b7d142de.JPG)

After that, it will ask for a master password which is shown in the figure below.

![fig2](https://user-images.githubusercontent.com/3108754/148324175-5d4af7dc-8ada-4504-933d-64ea8d16215f.JPG)

Then a random password for that particular website is created, encrypted and stored in the password database file. If there is no database file exits then it creates a database file and then stores the password. A screenshot for the scenario is shown in the figure below.

![fig3](https://user-images.githubusercontent.com/3108754/148324248-e151d671-3e5f-4fce-a008-3fac559ddbb8.JPG)

When the program is run with the same website again, it retrieves the password, decrypts it and shows it to the user. A screenshot is shown in the figure below.

![fig4](https://user-images.githubusercontent.com/3108754/148324310-5b68b847-01e8-41ac-8c2c-3d6caa1ac504.JPG)

In case if the user enters wrong master password it shows warning message and stops the program which is shown in the figure below.

![fig5](https://user-images.githubusercontent.com/3108754/148324362-8d16b603-8e47-4384-be4c-5d6899cfc461.JPG)

The program works the same way for any other website as it does for the first website. A screenshot for storing password for a different website in the same database is shown in the figure below.

![fig6](https://user-images.githubusercontent.com/3108754/148324411-5b8000a0-1f86-4923-bfb9-d8d0b4e1cd36.JPG)
