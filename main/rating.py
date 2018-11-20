'''
    Module which calculate new rating.
'''

def new_rating(r_a, r_b):
    '''
        r_a - first player rating\n
        r_b - second player rating\n
        Returns new player A rating and new player B rating\n
    '''
    k = 10
    math_expec_a = 1 / (1 + 10**((r_b - r_a) / 400))
    math_expec_b = 1 / (1 + 10**((r_a - r_b) / 400))
    new_r_a = r_a + k * (1 - math_expec_a)
    new_r_b = r_b + k * (0 - math_expec_b)
    return new_r_a, new_r_b
