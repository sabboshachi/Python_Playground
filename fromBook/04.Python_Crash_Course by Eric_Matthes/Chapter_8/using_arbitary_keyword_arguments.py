def build_profile(first, last, **user_info):
    """Bulid a dictioanry containig everithing er know about the user """
    profile = {}
    profile["first name "] = first
    profile["last name "] = last
    for key , value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile("sandy" , 'sarkar', location="india", field="scientist")
print(user_profile)