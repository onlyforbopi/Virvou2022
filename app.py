from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route("/new")
def indexw():
    return "Hello World2!"

# asdasdasdssdfsdfd
@app.route("/new/eirini")
def indexw2():
    return "xronia polla eirini!"



# endpoint for register
#       POST
#       CHECK IF USER ALREADY EXISTS
#       INSERT into users ....

# endpoint for login
#       POST
#       CHECK IF USER EXISTS && PASSWORD CORRECT KTL

# endpoint for favorites
#       GET
#       SELECT *
#       RETURNS: LIST OF FAVORITES

# endpoint to add favorite
#       POST
#       INSERT INTO FAVORITES


# SINGLE

    # FRONTEND / BACKEND / DB STO IDIO SISTIMA

# TWO TIER

    # FRONTEND - SYSTEM 1
        # EIRINI
            # VUE/HTML/JAVASCRIPT/CSS

            # 
            # API
            #

    # BACKEND + DB - SYSTEM 2ASDS
        # ALEXO + PANAGIS
            # DB = POSTGRESS
            # BACKEND = FLASK

