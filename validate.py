import psycopg2
def auth(userid,password):
    conn = psycopg2.connect("dbname=dc6e5dm4vjomup user=uolzycphiyghbl password=50a316c25c0ced815e8bbe6d8564c5d4ed044f89dcd2b2c9ac3fb1e4a4d38d12 host=ec2-50-16-108-41.compute-1.amazonaws.com port=5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_values WHERE username=%(user)s AND pass=%(passw)s;", {'user': userid, 'passw': password})
    response = cur.fetchall()
    if len(response) > 0:
        return True
    else:
        return False
