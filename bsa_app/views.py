from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def mechanical(request, equipment):
    equipment_data = [
        {"Equipment": "PAC-L01-01", "Status": 1, "Fault": 0},
        {"Equipment": "PAC-L01-02", "Status": 1, "Fault": 0},
        {"Equipment": "PAC-L01-03", "Status": 1, "Fault": 0},
        {"Equipment": "PAC-L01-04", "Status": 1, "Fault": 0},
        {"Equipment": "PAC-L01-05", "Status": 0, "Fault": 0},
        {"Equipment": "PAC-L01-06", "Status": 1, "Fault": 0},
        {"Equipment": "PAC-L01-07", "Status": 0, "Fault": 1},
    ]

    filtered_data = [item for item in equipment_data if item['Equipment'] == equipment]
    print(equipment)

    if request.GET.get('data') == 'status':
        return JsonResponse(filtered_data, safe=False)
    else:
        context = {
            'equipment': equipment,  
            'equipment_data': filtered_data,
        }
        return render(request, 'bsa_app/mechanical.html', context)
    # return render(request, 'bsa_app/mechanical.html', context)