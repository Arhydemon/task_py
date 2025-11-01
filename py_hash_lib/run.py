import hashlib
import time
LETTERS = "ABEKMHOPCTYX"
DIGITS = "0123456789"
REGIONS = [
    "01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19",
    "20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39",
    "40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59",
    "60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79",
    "80","81","82","83","84","86","87","89","90","91","92","93","94","95","96","97","98","99",
    "177","197","199","277","299","777","799","178","198","790"
]

def solve_problem(target_md5: str, target_sha256: str) -> str:
    start = time.time()
    total = len(LETTERS) * 1000 * (len(LETTERS) ** 2) * len(REGIONS)
    print("py_hash_lib/run.py")
    print(f"~{total/1000:.1f} тыс возможных результатов")
    md5 = hashlib.md5
    sha256 = hashlib.sha256
    for l1 in LETTERS:
        for d1 in DIGITS:
            for d2 in DIGITS:
                for d3 in DIGITS:
                    for l2 in LETTERS:
                        for l3 in LETTERS:
                            base = f"{l1}{d1}{d2}{d3}{l2}{l3}"
                            base_bytes = base.encode("utf-8")
                            for reg in REGIONS:
                                candidate_bytes_for_md5 = base_bytes + reg.encode("utf-8")
                                if md5(candidate_bytes_for_md5).hexdigest() == target_md5:
                                    candidate = base + reg
                                    if sha256(candidate.encode("utf-8")).hexdigest() == target_sha256:
                                        elapsed = time.time() - start
                                        print(f"|| {candidate} ||")
                                        print(f"Время выполнения функции {elapsed} сек.")
                                        return candidate
    elapsed = time.time() - start
    print("|| not found ||")
    print(f"Время выполнения функции {elapsed} сек.")
    return ""

if __name__ == "__main__":
    # MD5 (32 hex)
    target1 = "743f0ed26d2bff34fb9a335588238ceb"
    # SHA-256 (64 hex)
    target2 = "ef581243eb6f7fa74ce03466b9051464275c6b34017a6f031f2548a6d5d0b711"
    solve_problem(target1, target2)