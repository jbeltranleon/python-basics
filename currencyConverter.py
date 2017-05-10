def run():
	print('Currency Converter')
	print('Convert from MXN to COP')
	print('')

	ammount = float(input('Ammount (MXN): '))

	result = foreign_exchange_calculator(ammount)

	print('${} Mexican Pesos are ${} Colombian Pesos'.format(ammount, result))
	print('')


def foreign_exchange_calculator(ammount):
	mxn_to_cop_rate = 155

	return mxn_to_cop_rate * ammount

if __name__ == '__main__':
	run()