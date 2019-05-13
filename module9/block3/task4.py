def parse_db_url(db_link):
    params=db_link.split("://")
    if params[0]=="postgres":
        user=params[1].split(':')
        password,host=user[1].split('@')
        port,name=user[2].split('/')
        dic={
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': user[0],
            'PASSWORD': password,
            'HOST': host,
            'PORT': port,
            'NAME': name,
        }
        return dic
    elif params[0]=="sqlite":
        dic={
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': params[1][1:],
        }       
    else:
        raise ValueError
    for val in dic.values():
        if val=='':
            raise ValueError
    return dic






print(parse_db_url("postgres://admin:oocooSh7@postgres.host:5432/my_db"))
print(parse_db_url("sqlite:///C:/Users/admin/site_db.sqlite3"))
print(parse_db_url("sqlite:///"))

print(parse_db_url("postgres://admin:@postgres.host:5432/my_db"))