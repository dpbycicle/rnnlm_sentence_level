import reader
import sys
import os
import numpy as np


data = [4, 3, 2, 1, 0, 5, 6, 1, 1, 1, 1, 0, 3, 4, 1]
batch_size = 3
num_steps = 2

data_path = "/Users/xiaopeng/code/ptb/simple-examples/data"
def test():
	#train, test, vali, vocab = reader.ptb_raw_data(data_path)
	#print len(train), train[ : 100], vocab

	output = list(reader.ptb_iterator(data, 3, 2))
	#print len(x), x[0], len(y), y[0]
	print len(output)
	print len(output[0]), len(output[0][0]), len(output[0][1])
	print output[0][0], "\n"
	print output[0][1], "\n"
	print type(output)
	print output


print data	
if __name__ == "__main__":
	test()

