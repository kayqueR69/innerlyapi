def preencheUsuario(dadosUser, modelUser):

    for key, value in dadosUser.items():
        if (key not in ['id', 'email', 'senha']):
            modelUser[key] = dadosUser[key].upper()
    
    return modelUser