from story_visualization import StoryPlot
import h5py

story_plot = StoryPlot(stories_data_set_path='./dataset/vist_dataset/validate_data/val.story-in-sequence.json',
                       images_root_folder_path='./dataset/vist_dataset/validate_data')

train_dataset = h5py.File('./dataset/image_embeddings_to_sentence/stories_to_index_valid.hdf5', 'r')
story_ids = train_dataset['story_ids']
hypothesis = open('./results/hypotheses_2018-01-18_17:39:24-2018-01-20_18:50:39_valid.txt').read().split('\n')

story_index = 30

while True:
    story_id = story_ids[story_index]
    story_plot.visualize_story(str(story_id), hypothesis[(story_index * 5) : (story_index*5) + 5])

    direction = raw_input('Prev/Next q-w:')
    if direction == 'q':
        story_index = story_index - 5
    elif direction == 'w':
        story_index = story_index + 5
