$Action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c start_dashboard.bat"
$Trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName "GlobalBusinessProblemDashboard" -Action $Action -Trigger $Trigger
