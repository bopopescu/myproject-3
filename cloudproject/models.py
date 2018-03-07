import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def entry(x, y, z):
    table = dynamodb.Table('users')
    table.put_item(
        Item={
            'username': y,
            'emailid': x,
            'password': z,
            'check': 0
        }
    )

def validate(u, p):
    table = dynamodb.Table('users')
    response = table.scan(
        FilterExpression=Attr('username').eq(u) & Attr('password').eq(p) & Attr('check').eq(0)
    )
    items = response['Items']
    if len(items) > 0:
        return 1
    else:
        response = table.scan(
            FilterExpression=Attr('username').eq(u) & Attr('password').eq(p) & Attr('check').eq(1)
        )
        items1 = response['Items']
        if len(items1) > 0:
            return 2
        else:
            return 0

def delroom(u):
    table = dynamodb.Table('room')
    response = table.query(
        KeyConditionExpression=Key('roomId').eq(u)
    )
    items = response['Items']
    if len(items) > 0:
        table.delete_item(
            Key={
                'roomId': u,
            }
        )
        return 1
    else:
        return 0

def updateprice(u, p):
    table = dynamodb.Table('room')
    response = table.query(
        KeyConditionExpression=Key('roomId').eq(u)
    )
    items = response['Items']
    if len(items) > 0:
        table.update_item(
            Key={
                'roomId': u,
            },
            UpdateExpression='SET price = :val1',
            ExpressionAttributeValues={
                ':val1': p
            }
        )
        return 1
    else:
        return 0

def addRoom(t, p, a, c):
    table = dynamodb.Table('room')

    response = table.scan(
        FilterExpression=Attr('availability').eq('on') | Attr('availability').eq('off')
    )

    items = response['Items']

    num = len(items) + 1

    table.put_item(
        Item={
            'roomId': num,
            'type': t,
            'price': p,
            'availability': a,
            'capacity': c,
        }
    )

def findRoom(t):
    table = dynamodb.Table('room')

    response = table.scan(
        FilterExpression=Attr('type').eq(t) & Attr('availability').ne('off')
    )
    items = response['Items']
    if (len(items) < 0):
        return 0
    else:
        return (response['Items'][0]['roomId'])

def bookRoom(u, t, r, dt, d):
    table = dynamodb.Table('bookings')

    table.put_item(
        Item={
            'username': u,
            'roomId': r,
            'type': t,
            'date': dt,
            'days': d,
        }
    )

def availOff(r):
    table = dynamodb.Table('room')
    table.update_item(
        Key={
            'roomId': r,
        },
        UpdateExpression='SET availability = :val1',
        ExpressionAttributeValues={
            ':val1': 'off'
        }
    )
