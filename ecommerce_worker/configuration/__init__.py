import os

def get_overrides_filename(variable):
    """
    Get the name of the file containing configuration overrides
    from the provided environment variable.
    """
    filename = os.environ.get(variable)

    if filename is None:
        msg = 'Please set the {} environment variable.'.format(variable)
        raise EnvironmentError(msg)

    return filename
