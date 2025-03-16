# Librairie EPSIC

Web app écrite avec Django, pour la gestion d'une librairie

## Configuration
- Utiliser de préférence un environnement virtuel
- Les dépendances sont incluses dans le fichier requirements.txt

## Mise à jour de la DB

1. Pour créer la BD selon les modèles disponibles :
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Pour créer un superuser : 
   ```
   python manage.py createsuperuser
   ```

## Exécution
1. Exécuter l'app :
   ```
   python manage.py runserver
   ```
2. Consulter l'app @ `http://127.0.0.1:8000`
3. Exécuter les tests :
   ```
   python -m pytest -v
   ```

