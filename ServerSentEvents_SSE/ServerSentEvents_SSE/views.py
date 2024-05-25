from django.shortcuts import render
from django.http import StreamingHttpResponse
import time, json, random

def home(request):
    dinle(request)
    return render(request, 'screen.html')

def dinle(request):
    def event_stream():
        x = 1.00
        y = 1.05
        z = 1.23
        while True:
            xOld = x
            x = x + random.uniform(-0.05, 0.05)
            yOld = y
            y = y + random.uniform(-0.05, 0.05)
            zOld = z
            z = z + random.uniform(-0.05, 0.05)
            data = {
                'x_lira': round(x, 3),
                'y_lira': round(y, 3),
                'z_lira': round(z, 3),
                'arrow_x': '↑' if x > xOld else '↓',
                'arrow_y': '↑' if y > yOld else '↓',
                'arrow_z': '↑' if z > zOld else '↓'
            }
            yield 'data: %s\n\n' % json.dumps(data)
            time.sleep(2.4)

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response