import itertools

#rのみ変数
def combination_list(r):
    lis=range(1,10)
    result = []
    for conb in itertools.combinations(lis, r):
        result.append(list(conb)) #タプルをリスト型に変換
    print("9Crの組み合わせリスト")
    print(result)

#結果の確認
combination_list(2)

#nとrが変数

def combination_list_n(n,r):
    lis=range(1,n+1)
    result = []
    for conb in itertools.combinations(lis, r):
        result.append(list(conb)) #タプルをリスト型に変換
    print("nCrの組み合わせリスト")
    print(result)

#結果の確認
combination_list_n(9,2)
