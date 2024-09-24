lambda_function_handler = "lambda_function.lambda_handler"
lambda_memory_size = 512
lambda_runtime = "python3.10"
lambda_timeout = 180

lambda_functions= {
  DEV_environment_vls_ecs_upscaler={
    
    source_code_file_location = "code/manual_downscaler/lambda_function.py"
    schedule_rate = "cron(0/5 * * * ? *)"
    env_vars ={
      environment = "PROD"
      S3_BUCKET = "rotate-logs-to-s3"
      application_group = "Valere-Services"

    }
    tags = {
      "environment" = "DEV"
      "Terraform" = "true"
    }
  },

}
