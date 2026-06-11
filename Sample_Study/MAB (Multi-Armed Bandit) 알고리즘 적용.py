import numpy as np

# 각 추천 안(배너 A, 배너 B, 배너 C)의 클릭(Success) 및 미클릭(Failure) 횟수 예시 데이터
# 실제로는 Redis 나 RDB에 저장되어 실시간으로 업데이트됩니다.
bandit_stats = {
    "banner_A": {"success": 120, "failure": 880},  # 클릭률 약 12%
    "banner_B": {"success": 180, "failure": 820},  # 클릭률 약 18% (우세)
    "banner_C": {"success": 50,  "failure": 950}   # 클릭률 약 5%
}

def choose_best_banner_mab():
    """
    톰슨 샘플링을 통해 실시간으로 탐색(Exploration)과 수확(Exploitation)을 조율하며 
    가장 최적의 배너를 반환합니다.
    """
    best_variant = None
    max_sample = -1
    
    for variant, stats in bandit_stats.items():
        # 베타 분포(Beta Distribution)에서 샘플링 추출
        # 성공 횟수가 많을수록 높은 값이 나올 확률이 큼
        sample = np.random.beta(stats["success"] + 1, stats["failure"] + 1)
        
        if sample > max_sample:
            max_sample = sample
            best_variant = variant
            
    return best_variant  # 가장 스코어가 높은 배너 ID 반환 (확률적으로 B가 주로 뽑힘)