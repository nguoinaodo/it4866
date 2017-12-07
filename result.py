from util import load_pickle
import matplotlib.pyplot as plt

svm = load_pickle('result/svm/learning')
svm_lda_50 = load_pickle('result/svm-lda/50/learning')
svm_lda_20 = load_pickle('result/svm-lda/20/learning')
lda_20 = load_pickle('result/lda/20/learning')
lda_50 = load_pickle('result/lda/50/learning')
plt.plot(svm[0], svm[1], 'r', label='tfidf-svm')
plt.plot(svm_lda_50[0], svm_lda_50[1], 'b', label='lda50-svm')
plt.plot(svm_lda_20[0], svm_lda_20[1], 'y', label='lda20-svm')
plt.plot(lda_20[0], lda_20[1], 'c', label='lda20')
plt.plot(lda_50[0], lda_50[1], 'm', label='lda50')
plt.legend()
plt.xlabel('part of training data')
plt.ylabel('test f1 score')
plt.savefig('result1.png')
plt.show()