def build_profile(first,last,**user_info):      # user_info is an empty dictionary
    profile = {}
    profile ["First_name"] = first
    profile ["Last_name"] = last
    for key,value in user_info.items():
        profile[key] = value
        
    return profile


print(build_profile('albert', 'einstein',  location='princeton',field='physics'))