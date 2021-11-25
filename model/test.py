from predict_sen import get_sentiment 


# test
sen = '좆같은 하루네 이거 못하겠네'
predicted = get_sentiment(sen)
print(sen, predicted)

sen = '좋은 하루에요 다들 희망찬 하루되세요~~~!!'
predicted = get_sentiment(sen)
print(sen, predicted)

sen = '씨발 존나하기 싫네'
predicted = get_sentiment(sen)
print(sen, predicted)

sen = '해도해도 끝이 없네 해도해도 끝이 없네 해도해도 끝이 없네 해도해도 끝이 없네 해도해도 끝이 없네'
predicted = get_sentiment(sen)
print(sen, predicted)

sen = '해도해도 끝이 없네 오히려 좋아'
predicted = get_sentiment(sen)
print(sen, predicted)


sen = '하 사회활동을 꼭 해야만 하는 걸까?'
predicted = get_sentiment(sen)
print(sen, predicted)

sen = '하 따분하긴해도 지금이 좋아'
predicted = get_sentiment(sen)
print(sen, predicted)
