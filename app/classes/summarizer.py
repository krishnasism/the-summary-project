def summarize(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
   
    import app.classes.cleaner as cleaner
    import os 
        
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    
    stop_words = set(stopwords.words("english"))
    f=open(os.path.dirname(os.path.realpath(__file__))+"/stopwords.txt")
    for stops in f.read().split():
        stop_words.add(stops)
    #print(sentences)
    
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)
    
    true_k = 2
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)
    
    
    
    c1 = list()
    c2 = list()
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        #print ("Cluster %d:" % i)
        for ind in order_centroids[i, :10]:
            if(i == 0):
                c1.append(terms[ind])
            else:
                c2.append(terms[ind])
    
    #print("\n")
    #print("\n")
    #print("\n")
    
    #print("Cluster 1 :")
    #print(c1)
    #print("\n")
    #print("Cluster 2 : ")
    #print(c2)
    
    sentence_score={}
    sc = 1.0
    for sentence in sentences:
        sc=1.0
        for word in c1:
            #print("\n* "+ word)
            if word in sentence.lower():
                if sc<=0:
                    sc=0
                if sentence in sentence_score.keys():
                    sentence_score[sentence]+=sc
                    sc = sc-0.05
                    #print(sentence_score[sentence])
                else:
                    sentence_score[sentence]=sc
                    sc = sc-0.05
                    #print(sentence_score[sentence])
    
    
    #print(sentence_score)
    
    sum_total = 0
    for sentence in sentences:
        if(sentence in sentence_score.keys()):
            sum_total += sentence_score[sentence]
    #print(sum_total)
    
    #print("Sum total : " + str(sum_total))
    
    average_score = int(sum_total/len(sentence_score))
    #print("Average = "+str(average_score))
    
    summary = []    
    
    #change the value have more fun!
    for sentence in sentences:
        #print(sentence)
        if sentence in sentence_score.keys() and sentence_score[sentence] > 2.6 * average_score:
            summary.append(cleaner.clean(sentence))
    
    #print(summary)
    
    sentence_score2={}
    
    for sentence in sentences:
        sc=1.0
        for word in c2:
            #print("\n* "+ word)
            if word in sentence.lower():
                if sc<=0:
                    sc=0
                if sentence in sentence_score2.keys():
                    sentence_score2[sentence]+=sc
                    sc = sc-0.05
                    #print(sentence_score[sentence])
                else:
                    sentence_score2[sentence]=sc
                    sc = sc-0.05
                    #print(sentence_score[sentence])
    
    
    #print(sentence_score)
    
    sum_total = 0
    for sentence in sentences:
        if(sentence in sentence_score2.keys()):
            sum_total += sentence_score2[sentence]
    #print(sum_total)
    
    #print("Sum total : " + str(sum_total))
    
    average_score = int(sum_total/len(sentence_score2))
    #print("Average = "+str(average_score))
    
    #change the value have more fun!
    for sentence in sentences:
        #print(sentence)
        if sentence in sentence_score2.keys() and sentence_score2[sentence] > 2.6 * average_score:
            summary.append(cleaner.clean(sentence))
    
    return(summary)