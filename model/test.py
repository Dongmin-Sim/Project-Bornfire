from predict_sen import get_sentiment 


# test
sen = '진짜 화나는 하루네 이거 못하겠네'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])

sen = '좋은 하루에요 다들 희망찬 하루되세요~~~!!'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])

sen = '너무너무 싫어!'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])

sen = '해도해도 끝이 없네 해도해도 끝이 없네 해도해도 끝이 없네 해도해도 끝이 없네 해도해도 끝이 없네'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])

sen = '해도해도 끝이 없네 오히려 좋아'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])


sen = '하 사회활동을 꼭 해야만 하는 걸까?'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])

sen = '하 따분하긴해도 지금이 좋아'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])

sen = '배고파'
predicted = get_sentiment(sen)
print(sen, round(predicted[0], 2) * 100, '%', predicted[1])