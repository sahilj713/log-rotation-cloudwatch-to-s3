lambda_function_handler = "lambda_function.lambda_handler"
lambda_memory_size = 512
lambda_runtime = "python3.10"
lambda_timeout = 180

lambda_functions= {
  DEV_environment_vls_ecs_upscaler={
    
    source_code_file_location = "code/upscaler/lambda_function.py"
    schedule_rate = "cron(30 3 ? * MON-FRI *)"
    env_vars ={
      environment = "DEV"
      application_group = "Valere-Services"

    }
    tags = {
      "environment" = "DEV"
      "Terraform" = "true"
    }
  },

  DEV_environment_vls_ecs_downscaler={
    source_code_file_location = "code/downscaler/lambda_function.py"
    schedule_rate = "cron(30 18 ? * MON-FRI *)"
    env_vars ={
      environment = "DEV"
      application_group = "Valere-Services"

    }
    tags = {
      "environment" = "DEV"
      "Terraform" = "true"
    }
  },

  UAT_environment_ecs_upscaler={
    source_code_file_location = "code/upscaler/lambda_function.py"
    schedule_rate = "cron(30 3 ? * MON *)"
    env_vars ={
      environment = "UAT"
      application_group = "Valere-Services"
    }
    tags = {
      "environment" = "UAT"
      "Terraform" = "true"
    }
  },

    UAT_environment_ecs_downscaler={
    source_code_file_location = "code/downscaler/lambda_function.py"
    schedule_rate = "cron(30 23 ? * FRI *)"
    env_vars ={
      environment = "UAT"
      application_group = "Valere-Services"
    }
    tags = {
      "environment" = "UAT"
      "Terraform" = "true"
    }
  },

}
