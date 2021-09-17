# qrcode_term
QR code generator for terminal output

# Screenshot

From a terminal:

![alt text](https://user-images.githubusercontent.com/40133678/133773723-388893a3-3a02-4b4a-b804-cb16310bd5f5.png)

# CLI

```
> python src/qrcode_term/qrcode_term.py
███████████████████████████
███▀▀▀▀▀▀▀████▀▀█▀▀▀▀▀▀▀███
███ █▀▀▀█ ██▄▀█ █ █▀▀▀█ ███
███ █   █ ███ ▀▀█ █   █ ███
███ ▀▀▀▀▀ █ █▀█▀█ ▀▀▀▀▀ ███
███▀██▀█▀▀█▀█ ▀▀▀█▀████████
███▄▄ ▄▀▄▀▀▀▄▄ ██▄ ▄▀▀▄ ███
████▄██▀▄▀   ▀▀▄▀▄▀ ▄█▄▄███
███▀▀▀▀▀▀▀█▄█▀ ▀█▀▀▀▀ ▀████
███ █▀▀▀█ █▄ ▄█▀▀█▄███▄████
███ █   █ █▄ ▀█ █▀▄ ▄ ▄ ███
███ ▀▀▀▀▀ █▀█ ▄▀▄▀▀█▀█▀████
███████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Hello world!

> python src/qrcode_term/qrcode_term.py --data "mydata" -f5
███████████████████████████████
███████████████████████████████
█████▀▀▀▀▀▀▀██▀████▀▀▀▀▀▀▀█████
█████ █▀▀▀█ █▄  █ █ █▀▀▀█ █████
█████ █   █ █▀▀▄▀▀█ █   █ █████
█████ ▀▀▀▀▀ █▀▄▀▄▀█ ▀▀▀▀▀ █████
█████▀█▀█▀█▀██▀██▀███▀██▀██████
██████ ▀▀  ▀█  █ █ ▀ █  ▀ █████
█████ ▄█▄▀▄▀ ▀█▄ ▄ ▀ ▄██▀██████
█████▀▀▀▀▀▀▀█▄▄ █▀█▄▄▀█▀  █████
█████ █▀▀▀█ █▀█ █▀█ █▀██  █████
█████ █   █ █▀█▄ █ ▀   ▀▄▀█████
█████ ▀▀▀▀▀ █▀ ▀ ▄ ▀ ▀▀█ ▀█████
███████████████████████████████
███████████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
mydata

> python src/qrcode_term/qrcode_term.py --data "mydata 2" -f3 -i
                           
   ▄▄▄▄▄▄▄ ▄ ▄▄  ▄▄▄▄▄▄▄   
   █ ▄▄▄ █ ██▀█▀ █ ▄▄▄ █   
   █ ███ █ ▄▀▀▀▄ █ ███ █   
   █▄▄▄▄▄█ ▄ ▄▀█ █▄▄▄▄▄█   
   ▄  ▄▄▄▄▄▄██▀█▄  ▄ ▄▄▄   
    ▀▄▄█▀▄ ▄▀█ ▀ ▀█  ▄█▄   
   ▀▄▄ ▀▀▄▄▄▀ ▀ ▄▄▄█▄▀▀    
   ▄▄▄▄▄▄▄ █  ▀█▄▄▄█▀█▀    
   █ ▄▄▄ █ ██▀██▀▄█▀█▀ ▀   
   █ ███ █ ▀ █▀▀ ▄ ▄▀█▄▄   
   █▄▄▄▄▄█ ▄▀▄▄ ▀▀ ▄█▀▀▀   
                           
                           
mydata 2

> python src/qrcode_term/qrcode_term.py --data "mydata 3" -f10 -n
█████████████████████████████████████████
█████████████████████████████████████████
█████████████████████████████████████████
█████████████████████████████████████████
█████████████████████████████████████████
██████████ ▄▄▄▄▄ ██▄ ▀ █ ▄▄▄▄▄ ██████████
██████████ █   █ █ ▄ █▀█ █   █ ██████████
██████████ █▄▄▄█ █  ▄▄ █ █▄▄▄█ ██████████
██████████▄▄▄▄▄▄▄█ ▀▄▀ █▄▄▄▄▄▄▄██████████
██████████▄█▄▄▄▄▄█▀▄ █ █▄▄ ▄▄▀▀██████████
██████████▄ ▀  ▀▄▀█ ▄▄█▄▄ █   ███████████
██████████████▄▄▄█ █  ▀▀▀ ▀▀▀▄ ██████████
██████████ ▄▄▄▄▄ █▀▄▄▀ ▀ ▄█▀ ▄███████████
██████████ █   █ █ ▀██ ██ ▀█▀█▄██████████
██████████ █▄▄▄█ █▄▄▄▄█▄█▀█  ████████████
██████████▄▄▄▄▄▄▄█▄██▄█▄███▄█▄███████████
█████████████████████████████████████████
█████████████████████████████████████████
█████████████████████████████████████████
█████████████████████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
mydata 3
```
# API

Examples:
```
from qrcode_term import qrcode_string

a = qrcode_string("Is there anybody out there?")
b = qrcode_string("It's just another brick in the wall", frame_width=1)
c = qrcode_string("Vera! Vera!", version=5, inverse=True, frame_width=5, ansi_white=False)

print(a)
print(b)
print(c)
```

