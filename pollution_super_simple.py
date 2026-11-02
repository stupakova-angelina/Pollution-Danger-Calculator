sphere = input("Сфера (вода/воздух/почва): ").strip().lower()
pollutant = input("Загрязнение (нефть/пластик/бумага): ").strip().lower()


base_score = 50         
recovery_years = None   
recommendation = "Нужна экспертная оценка."


if pollutant == "нефть" or pollutant == "топливо":
    base_score = 95

   
    if sphere == "вода" or sphere == "море" or sphere == "океан":
        vuln_factor = 1.5
        recovery_years = 10000
        recommendation = "Срочно очистить водоём, сорбенты и боны."
    elif sphere == "почва" or sphere == "земля":
        vuln_factor = 1.0
        recovery_years = 50
        recommendation = "Убрать загрязнённый слой, биоремедиация."
    elif sphere == "воздух" or sphere == "атмосфера":
        vuln_factor = 1.2
        recovery_years = 15
        recommendation = "Поставить фильтры, перейти на чистое топливо."
    else:
        vuln_factor = 1.0 


elif pollutant == "пластик":
    base_score = 70
    if sphere == "вода":
        vuln_factor = 1.5
        recovery_years = 400
        recommendation = "Сбор мусора, заграждения на стоках."
    else:
        vuln_factor = 1.0


elif pollutant == "бумага":
    base_score = 30
    vuln_factor = 1.0
    recovery_years = 2
    recommendation = "Собрать и переработать."

else:
    vuln_factor = 1.0


danger = base_score * vuln_factor
if danger > 100:
    danger = 100


print("\n--- Результат ---")
print(f"Опасность: {danger}%")

if danger >= 85:
    print("МАКСИМАЛЬНЫЙ уровень опасности, срочно требуется помощь!!!")
elif danger >= 60:
    print("Высокий уровень опасности.")
elif danger >= 20:
    print("Средний уровень опасности.")
else:
    print("Низкий уровень опасности.")

print(f"Что делать: {recommendation}")
if recovery_years is not None:
    print(f"Природа восстановится примерно за {recovery_years} лет")
else:
    print("Точный срок восстановления неизвестен — нужна экспертная оценка.")
