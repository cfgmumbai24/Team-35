import React from 'react';
import './Modal.css'
import Modal from 'react-modal';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

const Modals = ({ modalIsOpen, closeModal, modalData }) => {
    const generatePdf = () => {
        const doc = new jsPDF();

        // Add title
        doc.setFontSize(18);
        doc.text('Description:', 10, 10);

        // Add steps
        doc.setFontSize(12);
        const steps = modalData?.steps?.split('\n') || [];
        steps.forEach((step, index) => {
            doc.text(`${index + 1}. ${step}`, 10, 20 + (index * 10));
        });

        // Save the PDF
        doc.save('steps.pdf');
    };

    return (
        <div className='main-modal'>
            <Modal
                isOpen={modalIsOpen}
                onRequestClose={closeModal}
                // style={customStyles}
                contentLabel="Example Modal"
            >
                <div className="modal-content">
                    <button onClick={closeModal} className="btn-close position-absolute top-2 end-2">X</button>
                    <div className="modal-header">
                        <h2 className="modal-title text-center w-100">{modalData?.title}</h2>
                    </div>
                    <div className="modal-body p-0">
                        <div className="embed-responsive embed-responsive-16by9">
                            <iframe
                                className="embed-responsive-item"
                                src={modalData.link}
                                title="YouTube video player"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                allowFullScreen
                            ></iframe>
                        </div>
                    </div>
                    <div id="content" className="modal-footer ">
                        <div className="text-gray-700 w-100 scrollable-div">
                            <h4>Description:</h4>
                            {modalData?.steps?.split('\n').map((step, index) => (
                                <p key={index} className="step-item">
                                    {step}
                                </p>
                            ))}
                        </div>
                    </div>
                    <button onClick={generatePdf} type="button" className="btn btn-primary">Download</button>
                </div>
            </Modal>
        </div>
    );
};

export default Modals;
