from sklearn import model_selection
from polls.views import readWeather
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

class Split:
    X = readWeather().values('airTemperature', 'pressure', 'humidity', 'precipitation', 'visibility',
                             'waterTemperature')
    y = readWeather().values('waveDirection', 'waveHeight', 'windWaveDirection', 'windDirection', 'windSpeed',
                             'wavePeriod')
    listX = []
    listY = []
    for x in X:
        listX.append(x)
    for Y in y:
        listY.append(Y)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(listX, listY, test_size=0.2, random_state=26)
    print(X_train)
    print(y_train)
  #  sc = StandardScaler()
  #  X_train = sc.fit_transform(X_train)
  #  X_test = sc.transform(X_test)

  # classifier = SVC(kernel='linear', random_state=0)
  #  classifier.fit(X_train, y_train)
  #  y_pred = classifier.predict(X_test)
  #  cm = confusion_matrix(y_test, y_pred)