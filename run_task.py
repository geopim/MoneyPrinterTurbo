import os
import sys
import uuid

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from app.models.schema import VideoParams, VideoAspect, VideoConcatMode
from app.services import task as tm

task_id = str(uuid.uuid4())

params = VideoParams(
    video_subject="O Fim da Foto no Cabide",
    video_script="Se você ainda tira foto de roupa no cabide ou esticada no chão, você está perdendo vendas todos os dias. A cliente não consegue imaginar como a peça fica no corpo. E eu sei que pagar estúdio e modelo profissional custa muito caro. Mas olha essa mágica: com o Estúdio de Inteligência Artificial do Revenda Moda, você sobe a foto da roupa no cabide, e em cinco segundos... bum! A IA veste a peça numa modelo virtual realista. Seu Instagram vai parecer catálogo de grife famosa, e você não gasta nenhum centavo a mais por isso. Quer testar? Clica no link do perfil e gera sua primeira foto de graça agora.",
    video_terms=["professional photographer studio", "clothes on a hanger", "artificial intelligence glowing", "fashion model posing", "smartphone shopping app"],
    video_aspect="9:16",
    video_concat_mode="random",
    video_clip_duration=5,
    video_count=1,
    video_language="pt",
    voice_name="pt-BR-AntonioNeural-Male",
    bgm_type="random",
    subtitle_enabled=True,
    font_name="STHeitiMedium.ttc",
    text_fore_color="#FFFF00"
)

print(f"Starting task {task_id}...")
result = tm.start(task_id=task_id, params=params)
print("Finished!")
print(result)
