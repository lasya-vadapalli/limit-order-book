print('enter number of levels:')
level=int(input())
print('enter each ask and its quantity:')
asks=dict(map(float,input().split())for _ in range(level))
sorted(asks)
print('enter each bid and its quantity:')
bids = dict(map(float, input().rstrip().split()) for _ in range(level))
sorted(bids,reverse=True)
print('enter A to ask, B to bid and C to cancel:')
aa=str(input())
print('enter MO for Market order and LO for limit order:')
t=str(input())
if(t=='MO'):
    if(aa=='C'):
        print('already bid executed')
    else:
        print('enter quantity:')    
        quantity=float(input())
        if(aa=='B'):
            q=quantity
            price=[]
            x=iter(asks.values())
            y=iter(asks.keys())
            sub=next(x)-q
            if(sub==0):
                price.append(next(y))
                asks.pop(next(y))
            elif(sub<0):
                asks.pop(next(y))
                q=abs(sub)
            else:
                asks[next(y)]= sub
                price.append(next(y))
            print(sum(price)/len(price))
        else:
            q=quantity
            price=[]
            x=iter(bids.values())
            y=iter(bids.keys())
            sub=next(x)-q
            if(sub==0):
                price.append(next(y))
                bids.pop(next(y))
            elif(sub<0):
                bids.pop(next(y))
                q=abs(sub)
            else:
                bids[next(y)]= sub
                price.append(next(y))
            print(sum(price)/len(price))
else:
    print('enter price quantity:')
    price,quantity=list(map(float,input().split()))
    if(aa=='A'):
        asks[price]=quantity
        sorted(asks)
        print('added to the queue')
    elif(aa=='B'):
        bids[price]=quantity
        sorted(bids)
        print('added to the queue')
    else:
        print('enter A to cancel Asks or B to cancel Bids:')
        z=str(input())
        if(z=='A'):
            x=iter(asks.values())
            y=iter(asks.keys())
            if(next(y)!=price):
                next
            else:
                if(price==next(y) and quantity==next(x)):
                    asks.pop(next(y))
        else:
            x=iter(bids.values())
            y=iter(bids.keys())
            if(next(y)!=price):
                next
            else:
                if(price==next(y) and quantity==next(x)):
                    bids.pop(next(y))




