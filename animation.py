


def animation(path):
    '''
    animation function contains the scripted folders that will be created for animation folder
    Parameter: path which it the directory path that is created by user 
    '''

    animation_path = path / "Animation" 
    animation_path.mkdir(parents=True, exist_ok=True)
    pre_production_path = animation_path / "Pre-production" 
    pre_production_path.mkdir(parents=True, exist_ok=True)
    idea_path = pre_production_path /"Idea"  
    idea_path.mkdir(parents=True, exist_ok=True) 
    script_path = pre_production_path /"Scripts"  
    script_path.mkdir(parents=True, exist_ok=True)  
    storyboard_path = pre_production_path /"Storyboard"  
    storyboard_path.mkdir(parents=True, exist_ok=True)  


    production_path = animation_path / "Production"  
    production_path.mkdir(parents=True, exist_ok=True) 
    illustration_path = production_path /"Illustration"  
    illustration_path.mkdir(parents=True, exist_ok=True)
    voice_casting_path = production_path /"Voice Casting"  
    voice_casting_path.mkdir(parents=True, exist_ok=True)
    animation = production_path /"Animation"  
    animation.mkdir(parents=True, exist_ok=True)


    post_production_path = animation_path / "Post Production"  
    post_production_path.mkdir(parents=True, exist_ok=True)
    sound_path = post_production_path /"Sound Effects"  
    sound_path.mkdir(parents=True, exist_ok=True)
    randering_path = post_production_path /"Randering"  
    randering_path.mkdir(parents=True, exist_ok=True)
    wrap_up_path = post_production_path /"Wrap-Up"  
    wrap_up_path.mkdir(parents=True, exist_ok=True)

    




