from gensim.models import word2vec

model = word2vec.Word2Vec.load_word2vec_format('/scratch/hwc25/eval6/bow2roy_prefix.vectors.add.txt', binary=False, unicode_errors='ignore')
#model.save("file.txt")
model.save_word2vec_format('/scratch/hwc25/eval6/sgns-bow2-8b-d500.vectors.add.bin', binary=True)
