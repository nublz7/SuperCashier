from SuperStore import *

custName = input('Masukan nama Anda: ')

trx = Runner(custName)
trx.welcome()
trx.input_item()
trx.input_choice()