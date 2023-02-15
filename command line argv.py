import sys

def print_variables():
    script_name = sys.argv[0]
    if len(sys.argv) > 1:
        variables = ' '.join(sys.argv[1:])
    else:
        variables = 'None'
    print("Script name:", script_name)
    print("Variables:", variables)
    print("Script name and variables:", script_name + ' ' + variables)


def helloWorld():
	print('Hello World')


helloWorld()
