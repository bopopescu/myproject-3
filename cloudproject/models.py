from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')


def entry(x, y, z):
    table = dynamodb.Table('users')
    table.put_item(
        Item={
            'username': y,
            'emailid': x,
            'password': z,
        }
    )


def validate(u, p):
    table = dynamodb.Table('users')
    response = table.scan(
        FilterExpression=Attr('emailid').eq(u) & Attr('password').eq(p)
    )
    items = response['Items']
    if len(items) > 0:
        return 2
    else:
        return 0

def addRoom(t, p, a,c):
    table = dynamodb.Table('rooms')

    response = table.scan(
        FilterExpression=Attr('avail').eq('on') | Attr('avail').eq('off')
    )

    items = response['Items']

    num = len(items) + 1

    table.put_item(
        Item={
            'roomNo': num,
            'type': t,
            'price': p,
            'avail': a,
            'capacity': c,
        }
    )