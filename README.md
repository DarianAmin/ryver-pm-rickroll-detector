# ryver-pm-rickroll-detector
Ryver bot to alert you if a rickroll link is sent to you in private messages.

## Getting started

### Clone this repository
To clone the repository, simply run this command in your preferred terminal:

```sh
$ git clone https://github.com/DarianAmin/ryver-pm-rickroll-detector.git
```

Now, navigate into this new directory:

```sh
$ cd ryver-pm-rickroll-detector
```

### Installing dependencies
The bot currently has two dependency, [`pyryver`](https://pypi.org/project/pyryver/) and [`requests`](https://pypi.org/project/requests/). Install it with the following commands:

```sh
$ pip install --upgrade pyryver
```

and 

```sh
pip install requests

or 

$ python -m pip install requests
```

### Adding your Ryver login
In the `main.py` file, you'll need to replace `Org_Name`, `Username`, and `Password` with their respective values.

For example, if you typically log into Ryver at `acme.ryver.com` with the username `important_ceo` and the password `password123`, these three values will be `acme`, `important_ceo`, and `password123` respectively.
