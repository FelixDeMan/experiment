import toml
import os
from sklearn.model_selection import ParameterGrid

def write_toml_lora():
    # Define the base configuration
    base_config = {
        'additional_network_arguments': {
            'network_module': "networks.lora",
        },
        'optimizer_arguments': {
            'learning_rate': 0.001,
            'lr_scheduler': "cosine_with_restarts",
            'lr_scheduler_num_cycles': 3,
            'lr_warmup_steps': 7,
            'optimizer_type': "AdamW8bit",
        },
        
        'training_arguments': {
            'max_train_epochs': 30,
            'save_every_n_epochs': 3,
            'save_last_n_epochs': 30,
            'train_batch_size': 3,
            'clip_skip': 2,
            'min_snr_gamma': 5.0,
            'weighted_captions': False,
            'seed': 42,
            'max_token_length': 225,
            'xformers': True,
            'lowram': True,
            'max_data_loader_n_workers': 8,
            'persistent_data_loader_workers': True,
            'save_precision': "fp16",
            'mixed_precision': "fp16",
            'output_name' : 'red_hugo_logo',
            'log_prefix' : 'red_hugo_logo',
            'save_state': False    
            },

        'model_arguments': {
            'pretrained_model_name_or_path': "runwayml/stable-diffusion-v1-5",
            'v2': False
            },
        
        'saving_arguments': {
            'save_model_as': "safetensors"
        },

        'dreambooth_arguments': {
            'prior_loss_weight': 1.0
        },

        'dataset_arguments': {
            'cache_latents': True

        }
    }
    hyperparameter_grid = {
        'unet_lr': [5e-6, 1e-4, 1e-5, 5e-5, 1e-6],
        'text_encoder_lr': [5e-6, 1e-4, 1e-5, 5e-5, 1e-6],
        'network_dim': [4, 8, 16, 32, 64],
    }

    # Create the grid of parameters
    grid = ParameterGrid(hyperparameter_grid)

    # Now you can loop over this grid and modify the TOML file with each combination of parameters
    for i, params in enumerate(grid):
        # Create a copy of the base configuration
        config = base_config.copy()

        # Update the copy with the current parameters
        config['additional_network_arguments'].update({
            'unet_lr': params['unet_lr'],
            'text_encoder_lr': params['text_encoder_lr'],
            'network_dim': params['network_dim'],
            'network_alpha': int(params['network_dim'] / 2),
        })

        # Create a directory name based on the current parameters
        directory_name = f"UNet{params['unet_lr']}TE{params['text_encoder_lr']}dim{params['network_dim']}".replace('.', '_')

        # Update the output and logging directories
        config['training_arguments'].update({
            'output_dir': os.path.join('runs_lora', directory_name).replace('\\', '/'),
            'logging_dir': os.path.join('runs_lora', directory_name, 'logs').replace('\\', '/'),
        })

        os.makedirs(config['training_arguments']['logging_dir'], exist_ok=True)

        # Add this configuration to the main file
        with open(os.path.join(config['training_arguments']['output_dir'], "training_config.toml"), 'w') as f:
            toml.dump(config, f)

write_toml_lora()