from heapq import heapify, heappop, heappush

def getNumberOfBacklogOrders(orders):
    buy = list()
    heapify(buy)
    sell = list()
    heapify(sell)

    for p, q, t in orders:
        if t == 0:  # 买单
            while q > 0 and len(sell) > 0:
                sp, sq = sell[0]
                if p < sp: break # 最小卖价高于当前买价，无法交易
                if sq > q:
                    sell[0] = (sp, sq - q)
                    q = 0
                    break
                else:
                    q -= sq
                    heappop(sell)
            if q != 0: heappush(buy, (-p, q))  # 将剩余的买单加入买单堆
        else:
            while q > 0 and len(buy) > 0:
                bp, bq = buy[0]
                if p > -bp: break
                if bq > q:
                    buy[0] = (bp, bq - q)
                    q = 0
                    break
                else:
                    q -= bq
                    heappop(buy)
            if q != 0: heappush(sell, (p, q))

    return (sum([x for _, x in buy]) + sum([x for _, x in sell])) % (10 ** 9 + 7)

quotes = [
    [[10,5,0],[15,2,1],[25,1,1],[30,4,0]],
    [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
]

for q in quotes:
    print(getNumberOfBacklogOrders(q))