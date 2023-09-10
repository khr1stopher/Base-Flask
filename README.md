# Base-Flask 
base project to create flask apps


```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requeriments.txt
flask db upgrade
```

```sh
flask shell
from app import db
from app.models import Prefijos

sr = Prefijos(keyx=1, fechaalta="2019-08-21 22:25:49.447424", prefijo="Sr.                                     ")
sra = Prefijos(keyx=2, fechaalta="2019-08-21 22:25:49.465618", prefijo="Sra.                                    ")
srta = Prefijos(keyx=3, fechaalta="2019-08-21 22:25:49.476792", prefijo="Srta.                                   ")

# Add the instances to the session and commit the changes to the database
db.session.add_all([sr,sra,srta])
db.session.commit()
```