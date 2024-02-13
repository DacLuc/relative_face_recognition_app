from insightface.app import FaceAnalysis
import cv2
import numpy as np
from numpy.linalg import norm


class FaceRecognitionController:
    def __init__(self):
        self.face_analysis = FaceAnalysis(
            name="buffalo_l",
            allowed_modules=["detection", "embedding", "recognition"],
            providers=["CPUExecutionProvider"],
        )
        self.face_analysis.prepare(ctx_id=-1, det_thresh=0.5, det_size=(640, 640))

    def check_has_faces(self, user_uploaded_img: str):
        image = cv2.imread(user_uploaded_img)
        faces = self.face_analysis.get(image)
        return len(faces) == 1

    def get_face_feature(self, user_uploaded_img: str):
        image = cv2.imread(user_uploaded_img)
        faces = self.face_analysis.get(image)
        if len(faces) > 0:
            face = faces[0]
            feature = face["embedding"]
            print(len(np.array(feature)))
            return np.array(feature)
        return None

    def compare_embeddings(self, embeddings_1: np.array, embeddings_2: np.array):
        embeddings_1 = embeddings_1.reshape(1, -1)
        embeddings_2 = embeddings_2.reshape(1, -1)
        similarity = np.dot(embeddings_1, embeddings_2.T) / (
            norm(embeddings_1) * norm(embeddings_2)
        )
        return similarity

    def check_similarity(self, image_path_1, image_path_2):
        vector_1 = self.get_face_feature(image_path_1)
        vector_2 = self.get_face_feature(image_path_2)
        if vector_1 is not None and vector_2 is not None:
            similarity = self.compare_embeddings(vector_1, vector_2)
            if similarity >= 0.8:
                return True
        return False
