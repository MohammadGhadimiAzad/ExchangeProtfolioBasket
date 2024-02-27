dir = "target_directory"
regressor.save(dir) # it will save a .pb file with assets and variables folders 

regressor = tf.keras.models.load_model(dir)

