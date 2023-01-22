TESTCASE_1 = 1,2,[10,3,6,6]
TESTCASE_2 = 20,5,[1,6,10,4]
TESTCASE_3 = 0,13,[4,6,3,7]


def main():
    balance_weights()


def balance_weights(left=0, right=0, weights=[]):
    start_weight_scale = 0
    balanced_scale = left + right
    sorted(weights)
    for (counter, item) in enumerate(weights):
        for additionItem in weights[counter:]:
            if(item + additionItem == balanced_scale):
                if start_weight_scale:
                    left = left + (item + additionItem)
                else:
                    right = right + (item + additionItem)
                return True

if balance_weights(0,13,[4,6,3,7]):
	print('We are able to balance the scale!')
else:
	print('We are UNABLE to balance the scale! :(')

if __name__ == "__main__":
    main()

