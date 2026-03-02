def lang_genoeg(lengte):
    return print('Je bent lang genoeg voor de attractie!') if lengte >= 120 else print('Sorry, je bent te klein!')
lang_genoeg(int(input('Hoelang ben je: ')))