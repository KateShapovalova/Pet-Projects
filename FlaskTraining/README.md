### Work with db:

- ```flask db init```

- ```flask db migrate -m "comment text"```

- ```flask db upgrade```

### If you want to make changes in translation:
- edit ".po" file in app\translations\LANG_CODE\LC_MESSAGES
- then run ```flask translate update```  and ```flask translate compile```
- rerun the application to see changes