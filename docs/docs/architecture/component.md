```puml
@startuml devices_api
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml

Container(devices_api, "API Сервис интеграции с устройствами", "Java") {
  Component(api, "API Controller", "REST Контроллер управления устройствами")
  Component(rtsp, "RTSP/TCP Controller", "Контроллер видеопотока с камеры")
  Component(control_device_service, "Сервис управления устройствами", "Управление устройствами")
  Component(integration, "Сервис интеграции", "Взаимодействие с внешними устройствами")
}

Rel(api, control_device_service, "Передаёт команды управления")
Rel(rtsp, control_device_service, "Получает видеопоток с камеры")
Rel(control_device_service, integration, "Взаимодействует с внешним устройством")
@enduml
```