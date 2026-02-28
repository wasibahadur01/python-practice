import numpy as np
import matplotlib.pyplot as plt
new_inputs = np.arrange(0, 10, 0.1).reshape(-1, 1)
plt.plot(new_inputs. model.predict(new_inputs), color='red')
plt.scatter(X, y, color='blue')
plt.title('Decision Boundary')



yhat = lm.predict(new_inputs)
plt.plot(new_inputs, yhat, color='red')