import sys
def my_print(*args, sep=' ', end='\n'):
    """Custom print function that prints each argument separated by a separator and ending with a newline by default."""
    output_str = sep.join(str(arg) for arg in args)
    output_str += end
    if sys.platform.startswith('win'):
        sys.stdout.write(output_str.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
    else:
        sys.stdout.write(output_str)
    sys.stdout.flush()
