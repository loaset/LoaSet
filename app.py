import streamlit as st
import pandas as pd

# 화면 넓게 쓰기
st.set_page_config(layout="wide", page_title="LoaSet Sim")

# === 1. 상단: 점수 및 기본 스펙 (이미지 좌측 상단 참고) ===
col_score, col_equip = st.columns([1, 3])

with col_score:
    st.metric(label="👑 전투력 (Simulation)", value="6,139.78", delta="5602.65 (인게임)")
    st.info("환수사 / 1680.00")

with col_equip:
    # 장비 아이콘 나열 (가짜 데이터로 UI만 구현)
    st.write("⚔️ **착용 장비 & 보석**")
    cols = st.columns(11) # 11칸으로 쪼개서 아이콘 배치
    for i in range(11):
        with cols[i]:
            st.button(f"💎", key=f"gem_{i}", help="10멸화: 데미지 44% 증가")

st.divider()

# === 2. 메인: 아크 패시브 & 각인 시뮬레이터 ===
c1, c2, c3 = st.columns([1, 1, 1])

# [왼쪽] 진화/깨달음/도약 선택 트리 (이미지 우측 하단 참고)
with c1:
    st.subheader("🌲 아크 패시브 (깨달음)")
    
    # 예: 깨달음 2티어 '깨어난 잠재력' 
    st.write("**2티어: 깨어난 잠재력** (치적 증가)")
    passive_level = st.select_slider(
        "레벨 선택", options=[0, 1, 2, 3], value=3, key="pass_1"
    )
    
    # 선택한 레벨에 따른 효과 미리보기
    if passive_level > 0:
        effect_val = passive_level * 10 # 10, 20, 30%
        st.caption(f"✅ 둔갑 스킬 치명타 적중률 **+{effect_val}%** 적용 중")

# [중간] 각인 및 전투 특성 (이미지 우측 상단 참고)
with c2:
    st.subheader("🔥 각인 & 특성")
    st.text("원한 Lv.3")
    st.text("돌격대장 Lv.3")
    st.progress(85, text="진화 포인트 (85%)") # 이미지의 게이지 바 구현

# [오른쪽] 실시간 계산 결과 (이미지 좌측 하단 통계 참고)
with c3:
    st.subheader("📊 시뮬레이션 결과")
    
    # 버킷 시스템으로 합산된 최종 수치
    st.write(f"치명타 적중률: **{65.0 + (passive_level * 10)}%**") # 기본 65 + 패시브
    st.write("치명타 피해: **285.0%**")
    st.write("최종 공격력: **194,441**")
    
    st.success("예상 DPS: **4,200만** (상위 5%)")
